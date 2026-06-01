#!/usr/bin/env python3
"""
TermMux-CLI CLI 入口点
CLI entry point for TermMux-CLI
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.core import main

if __name__ == "__main__":
    main()
