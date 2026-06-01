"""
TermMux-CLI 测试套件
Tests for TermMux-CLI
"""

import pytest
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestWorkspace:
    """工作区测试"""

    def test_workspace_creation(self):
        """测试工作区创建"""
        from src.workspace import Workspace

        ws = Workspace(name="测试工作区")
        assert ws.name == "测试工作区"
        assert ws.id is not None
        assert len(ws.panes) == 0

    def test_workspace_add_pane(self):
        """测试添加窗格"""
        from src.workspace import Workspace
        from src.pane import Pane

        ws = Workspace(name="测试工作区")
        pane = Pane(title="测试窗格")
        ws.add_pane(pane)

        assert len(ws.panes) == 1
        assert ws.get_active_pane() == pane

    def test_workspace_focus_pane(self):
        """测试窗格切换"""
        from src.workspace import Workspace
        from src.pane import Pane

        ws = Workspace(name="测试工作区")
        pane1 = Pane(title="窗格1")
        pane2 = Pane(title="窗格2")
        ws.add_pane(pane1)
        ws.add_pane(pane2)

        assert ws.active_pane_index == 1  # 最后添加的

        ws.focus_next_pane()
        assert ws.active_pane_index == 0

        ws.focus_prev_pane()
        assert ws.active_pane_index == 1

    def test_workspace_serialization(self):
        """测试工作区序列化"""
        from src.workspace import Workspace

        ws = Workspace(name="测试工作区")
        data = ws.to_dict()

        assert data["name"] == "测试工作区"
        assert "id" in data
        assert "panes" in data


class TestPane:
    """窗格测试"""

    def test_pane_creation(self):
        """测试窗格创建"""
        from src.pane import Pane, SplitDirection

        pane = Pane(title="测试窗格")
        assert pane.title == "测试窗格"
        assert pane.split_direction == SplitDirection.VERTICAL

    def test_pane_serialization(self):
        """测试窗格序列化"""
        from src.pane import Pane

        pane = Pane(title="测试窗格", command="ls -la")
        data = pane.to_dict()

        assert data["title"] == "测试窗格"
        assert data["command"] == "ls -la"


class TestAgentDetector:
    """Agent检测器测试"""

    def test_agent_status_enum(self):
        """测试Agent状态枚举"""
        from src.agent import AgentStatus

        assert AgentStatus.IDLE.value == "idle"
        assert AgentStatus.WORKING.value == "working"
        assert AgentStatus.BLOCKED.value == "blocked"
        assert AgentStatus.DONE.value == "done"

    def test_detected_agent_creation(self):
        """测试检测到的Agent创建"""
        from src.agent import DetectedAgent, AgentStatus

        agent = DetectedAgent(
            name="Claude Code",
            pid=12345,
            status=AgentStatus.WORKING,
            command="claude",
        )

        assert agent.name == "Claude Code"
        assert agent.pid == 12345
        assert agent.status == AgentStatus.WORKING

    def test_agent_detector_initialization(self):
        """测试Agent检测器初始化"""
        from src.agent import AgentDetector

        detector = AgentDetector()
        assert detector.detected_agents == []


class TestConfig:
    """配置测试"""

    def test_config_creation(self):
        """测试配置创建"""
        from src.config import Config
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            config = Config(config_dir=Path(tmpdir))
            assert config.theme == "default"
            assert config.show_status_bar is True

    def test_config_serialization(self):
        """测试配置序列化"""
        from src.config import Config
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            config = Config(config_dir=Path(tmpdir))
            data = config.to_dict()

            assert "theme" in data
            assert "show_status_bar" in data


class TestPaneManager:
    """窗格管理器测试"""

    def test_pane_manager_creation(self):
        """测试窗格管理器创建"""
        from src.pane import PaneManager

        manager = PaneManager()
        assert len(manager.panes) == 0

    def test_create_pane(self):
        """测试创建窗格"""
        from src.pane import PaneManager

        manager = PaneManager()
        pane = manager.create_pane(title="新窗格")

        assert pane is not None
        assert len(manager.panes) == 1

    def test_split_pane(self):
        """测试分割窗格"""
        from src.pane import PaneManager, SplitDirection

        manager = PaneManager()
        pane = manager.create_pane(title="原始窗格")
        new_pane = manager.split_pane(pane.id, SplitDirection.HORIZONTAL)

        assert new_pane is not None
        assert len(manager.panes) == 2

    def test_close_pane(self):
        """测试关闭窗格"""
        from src.pane import PaneManager

        manager = PaneManager()
        pane1 = manager.create_pane(title="窗格1")
        pane2 = manager.create_pane(title="窗格2")

        result = manager.close_pane(pane2.id)
        assert result is True
        assert len(manager.panes) == 1


class TestWorkspaceManager:
    """工作区管理器测试"""

    def test_workspace_manager_creation(self):
        """测试工作区管理器创建"""
        from src.workspace import WorkspaceManager

        manager = WorkspaceManager()
        assert len(manager.workspaces) == 0

    def test_create_workspace(self):
        """测试创建工作区"""
        from src.workspace import WorkspaceManager

        manager = WorkspaceManager()
        ws = manager.create_workspace("新工作区")

        assert ws is not None
        assert len(manager.workspaces) == 1
        assert manager.get_active_workspace() == ws


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
