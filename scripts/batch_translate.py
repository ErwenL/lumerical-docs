#!/usr/bin/env python3
"""
批量翻译脚本 - 自动处理所有未翻译的LSF命令文档。
"""

import argparse
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# 尝试导入requests，如果不可用则警告
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("警告: requests未安装，API翻译功能将不可用")

# 尝试导入googletrans，如果不可用则使用备用方案
try:
    from googletrans import Translator
    HAS_GOOGLETRANS = True
except ImportError:
    HAS_GOOGLETRANS = False
    print("警告: googletrans未安装，将创建模板文件而不翻译内容")
    print("安装命令: pip install googletrans==4.0.0rc1")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
EN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "en"
CN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "cn"
PROGRESS_FILE = PROJECT_ROOT / "docs" / "translation-progress.json"
BATCH_LOG_FILE = PROJECT_ROOT / "docs" / "batch_translation_log.json"


class BatchTranslator:
    """批量翻译器，处理多个文档的翻译。"""
    
    def __init__(self, use_api: bool = False, api_key: Optional[str] = None):
        """初始化翻译器。
        
        Args:
            use_api: 是否使用翻译API（默认为False，使用免费翻译）
            api_key: 翻译API密钥（如果需要）
        """
        self.use_api = use_api
        self.api_key = api_key
        self.translated_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        
        # 初始化翻译器
        if HAS_GOOGLETRANS:
            self.translator = Translator()
        else:
            self.translator = None
        
    def translate_text(self, text: str, source_lang: str = 'en', target_lang: str = 'zh-cn') -> str:
        """翻译文本内容。
        
        Args:
            text: 要翻译的文本
            source_lang: 源语言代码
            target_lang: 目标语言代码
            
        Returns:
            翻译后的文本
        """
        try:
            if not self.translator:
                # 如果没有翻译器，返回原文（但添加标记）
                return f"[待翻译] {text}"
            
            if self.use_api and self.api_key:
                # 使用付费API（如果有）
                return self._translate_with_api(text, source_lang, target_lang)
            else:
                # 使用免费翻译
                return self._translate_with_googletrans(text, source_lang, target_lang)
        except Exception as e:
            logger.warning(f"翻译失败，返回原文: {e}")
            return text
    
    def _translate_with_googletrans(self, text: str, source_lang: str, target_lang: str) -> str:
        """使用googletrans进行翻译。"""
        try:
            # 避免翻译代码块和特殊格式
            if self._should_skip_translation(text):
                return text
            
            if not self.translator:
                return f"[待翻译] {text}"
                
            translation = self.translator.translate(text, src=source_lang, dest=target_lang)
            return translation.text
        except Exception as e:
            logger.error(f"Google翻译失败: {e}")
            return text
    
    def _translate_with_api(self, text: str, source_lang: str, target_lang: str) -> str:
        """使用翻译API进行翻译。"""
        # 如果没有翻译器，返回待翻译标记
        if not self.translator:
            return f"[待翻译] {text}"
        
        # 这里可以集成其他翻译API
        # 暂时使用googletrans作为后备
        return self._translate_with_googletrans(text, source_lang, target_lang)
    
    def _should_skip_translation(self, text: str) -> bool:
        """检查是否应该跳过翻译（如代码块、URL等）。"""
        skip_patterns = [
            'http://', 'https://', 'ftp://',
            '`', '```', '    ', '\t',  # 代码块
            '# ', '## ', '### ',  # Markdown标题
            '![', '](',  # 图片标记
            '<', '>',  # HTML标签
        ]
        
        text_lower = text.lower()
        for pattern in skip_patterns:
            if pattern in text:
                return True
        
        # 如果文本太短或主要是符号，跳过
        if len(text.strip()) < 3:
            return True
            
        return False
    
    def translate_document(self, en_file: Path, cn_file: Path, overwrite: bool = False) -> bool:
        """翻译单个文档。
        
        Args:
            en_file: 英文文档路径
            cn_file: 中文文档路径
            overwrite: 是否覆盖已存在的中文文件
            
        Returns:
            是否成功
        """
        # 检查中文文件是否已存在
        if cn_file.exists() and not overwrite:
            logger.info(f"中文文件已存在，跳过: {cn_file.name}")
            self.skipped_count += 1
            return False
        
        # 检查英文文件是否存在
        if not en_file.exists():
            logger.error(f"英文文件不存在: {en_file}")
            self.failed_count += 1
            return False
        
        try:
            # 读取英文内容
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 分析文档结构并翻译
            translated_content = self._translate_document_content(content, en_file.stem)
            
            # 确保中文目录存在
            cn_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入中文文件
            with open(cn_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            
            logger.info(f"翻译完成: {en_file.name} -> {cn_file.name}")
            self.translated_count += 1
            return True
            
        except Exception as e:
            logger.error(f"翻译文档失败 {en_file.name}: {e}")
            self.failed_count += 1
            return False
    
    def _translate_document_content(self, content: str, command_name: str) -> str:
        """翻译文档内容，保留格式和结构。"""
        lines = content.split('\n')
        translated_lines = []
        
        # 添加翻译元数据
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        translated_lines.append('<!--')
        translated_lines.append(f'Translation from English documentation')
        translated_lines.append(f'Original command: {command_name}')
        translated_lines.append(f'Translation date: {timestamp}')
        translated_lines.append(f'Automated translation')
        translated_lines.append('-->')
        translated_lines.append('')
        
        in_code_block = False
        in_table = False
        
        for line in lines:
            # 跳过空行
            if not line.strip():
                translated_lines.append(line)
                continue
            
            # 处理代码块
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                translated_lines.append(line)
                continue
            
            if in_code_block:
                # 代码块内的内容不翻译
                translated_lines.append(line)
                continue
            
            # 处理表格行
            if '|' in line and '---' in line:
                # 表格分隔行，不翻译
                translated_lines.append(line)
                in_table = True if '---' in line else False
                continue
            
            if '|' in line and in_table:
                # 表格内容行，只翻译描述部分
                parts = line.split('|')
                if len(parts) >= 3:
                    # 第一列通常是语法，第二列是描述
                    translated_parts = []
                    for i, part in enumerate(parts):
                        if i == 2 and part.strip():  # 描述列
                            translated = self.translate_text(part.strip())
                            translated_parts.append(f' {translated} ')
                        else:
                            translated_parts.append(part)
                    translated_lines.append('|'.join(translated_parts))
                else:
                    translated_lines.append(line)
                continue
            
            # 处理标题行
            if line.startswith('# '):
                title = line[2:].strip()
                translated_title = self.translate_text(title)
                translated_lines.append(f'# {translated_title}')
                continue
            
            if line.startswith('## '):
                title = line[3:].strip()
                translated_title = self.translate_text(title)
                translated_lines.append(f'## {translated_title}')
                continue
            
            if line.startswith('### '):
                title = line[4:].strip()
                translated_title = self.translate_text(title)
                translated_lines.append(f'### {translated_title}')
                continue
            
            # 普通文本行
            translated_line = self.translate_text(line)
            translated_lines.append(translated_line)
        
        return '\n'.join(translated_lines)
    
    def get_untranslated_commands(self) -> List[str]:
        """获取所有未翻译的命令列表。"""
        if not EN_DOCS_DIR.exists():
            logger.error(f"英文文档目录不存在: {EN_DOCS_DIR}")
            return []
        
        # 创建中文目录（如果不存在）
        CN_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        
        # 获取文件列表
        en_files = {f.stem for f in EN_DOCS_DIR.glob("*.md")}
        cn_files = {f.stem for f in CN_DOCS_DIR.glob("*.md")}
        
        # 找出未翻译的文件
        untranslated = sorted(en_files - cn_files)
        return untranslated
    
    def batch_translate(self, limit: Optional[int] = None, overwrite: bool = False) -> Dict:
        """批量翻译所有未翻译的命令。
        
        Args:
            limit: 限制翻译的数量（None表示全部）
            overwrite: 是否覆盖已存在的文件
            
        Returns:
            翻译统计信息
        """
        logger.info("开始批量翻译...")
        
        # 获取未翻译的命令
        untranslated = self.get_untranslated_commands()
        total_untranslated = len(untranslated)
        
        if total_untranslated == 0:
            logger.info("所有命令都已翻译完成！")
            return {"status": "complete", "translated": 0, "failed": 0, "skipped": 0}
        
        logger.info(f"发现 {total_untranslated} 个未翻译命令")
        
        # 应用限制
        if limit and limit < total_untranslated:
            untranslated = untranslated[:limit]
            logger.info(f"限制翻译前 {limit} 个命令")
        
        # 重置计数器
        self.translated_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        
        # 翻译每个命令
        start_time = time.time()
        results = []
        
        for i, command in enumerate(untranslated, 1):
            logger.info(f"处理 ({i}/{len(untranslated)}): {command}")
            
            en_file = EN_DOCS_DIR / f"{command}.md"
            cn_file = CN_DOCS_DIR / f"{command}.md"
            
            success = self.translate_document(en_file, cn_file, overwrite)
            results.append({
                "command": command,
                "success": success,
                "timestamp": datetime.now().isoformat()
            })
            
            # 添加延迟避免请求过快
            time.sleep(0.5)
        
        elapsed_time = time.time() - start_time
        
        # 生成统计信息
        stats = {
            "total_untranslated": total_untranslated,
            "processed": len(untranslated),
            "translated": self.translated_count,
            "failed": self.failed_count,
            "skipped": self.skipped_count,
            "elapsed_time_seconds": round(elapsed_time, 2),
            "timestamp": datetime.now().isoformat()
        }
        
        # 保存日志
        self._save_batch_log(results, stats)
        
        logger.info(f"批量翻译完成！")
        logger.info(f"统计: 处理 {len(untranslated)} 个, 翻译 {self.translated_count} 个, "
                   f"失败 {self.failed_count} 个, 跳过 {self.skipped_count} 个")
        logger.info(f"耗时: {elapsed_time:.2f} 秒")
        
        return stats
    
    def _save_batch_log(self, results: List[Dict], stats: Dict) -> None:
        """保存批量翻译日志。"""
        log_data = {
            "batch_id": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "statistics": stats,
            "results": results
        }
        
        try:
            with open(BATCH_LOG_FILE, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
            logger.info(f"批量翻译日志已保存: {BATCH_LOG_FILE}")
        except Exception as e:
            logger.error(f"保存日志失败: {e}")


def main() -> None:
    """主入口函数。"""
    parser = argparse.ArgumentParser(
        description="LSF脚本文档批量翻译工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 翻译所有未翻译的命令（不覆盖已存在的文件）
  python scripts/batch_translate.py
  
  # 翻译前10个未翻译的命令
  python scripts/batch_translate.py --limit 10
  
  # 翻译所有命令，覆盖已存在的文件
  python scripts/batch_translate.py --overwrite
  
  # 使用翻译API（需要配置API密钥）
  python scripts/batch_translate.py --use-api
  
  # 显示未翻译命令列表
  python scripts/batch_translate.py --list
        """
    )
    
    # 操作参数
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="限制翻译的数量（默认：全部）"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="覆盖已存在的中文文件"
    )
    parser.add_argument(
        "--use-api",
        action="store_true",
        help="使用翻译API（需要配置）"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="翻译API密钥"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="显示未翻译命令列表"
    )
    
    args = parser.parse_args()
    
    # 确保中文目录存在
    CN_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 创建翻译器
    translator = BatchTranslator(use_api=args.use_api, api_key=args.api_key)
    
    if args.list:
        # 显示未翻译命令列表
        untranslated = translator.get_untranslated_commands()
        print(f"\n未翻译命令总数: {len(untranslated)}")
        for i, cmd in enumerate(untranslated[:50], 1):
            print(f"{i:3d}. {cmd}")
        if len(untranslated) > 50:
            print(f"... 还有 {len(untranslated) - 50} 个命令")
    else:
        # 执行批量翻译
        stats = translator.batch_translate(limit=args.limit, overwrite=args.overwrite)
        
        # 显示摘要
        print("\n" + "=" * 60)
        print("批量翻译摘要")
        print("=" * 60)
        print(f"未翻译命令总数: {stats['total_untranslated']}")
        print(f"本次处理数量: {stats['processed']}")
        print(f"成功翻译: {stats['translated']}")
        print(f"翻译失败: {stats['failed']}")
        print(f"跳过（已存在）: {stats['skipped']}")
        print(f"耗时: {stats['elapsed_time_seconds']} 秒")
        print("=" * 60)


if __name__ == "__main__":
    main()