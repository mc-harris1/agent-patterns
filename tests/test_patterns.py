from agent_patterns import (
    PlanExecutePattern,
    ReActPattern,
    ReflectionPattern,
    RouterPattern,
    SupervisorPattern,
)


def test_pattern_exports() -> None:
    assert ReActPattern().name == "react"
    assert PlanExecutePattern().name == "plan_execute"
    assert SupervisorPattern().name == "supervisor"
    assert RouterPattern().name == "router"
    assert ReflectionPattern().name == "reflection"


def test_placeholder_run_messages() -> None:
    assert "TODO" in ReActPattern().run("solve")
    assert "TODO" in PlanExecutePattern().run("plan")
    assert "TODO" in SupervisorPattern().run("delegate")
    assert "TODO" in RouterPattern().run("route")
    assert "TODO" in ReflectionPattern().run("revise")
