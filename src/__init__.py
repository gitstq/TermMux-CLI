#!/usr/bin/env python3
"""
TermMux-CLI - 轻量级终端多路复用与AI Agent感知管理器
Lightweight Terminal Multiplexer with AI Agent Awareness

灵感来源于 herdr (https://github.com/ogulcancelik/herdr)
用 Python 实现，更易于安装和扩展
"""

__version__ = "1.0.0"
__author__ = "gitstq"
__license__ = "MIT"

from .core import TermMux
from .workspace import Workspace, WorkspaceManager
from .pane import Pane, PaneManager
from .agent import AgentDetector, AgentStatus
from .session import SessionManager

__all__ = [
    "TermMux",
    "Workspace",
    "WorkspaceManager",
    "Pane",
    "PaneManager",
    "AgentDetector",
    "AgentStatus",
    "SessionManager",
]
