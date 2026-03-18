from __future__ import annotations

import json
from pathlib import Path


class WriteTool:
    name = "Write"
    description = "Write content to a file. ALWAYS use this to create scripts or config files instead of using Bash with echo/cat."

    def prompt_block(self) -> str:
        schema = {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "The file path to write to"},
                "content": {"type": "string", "description": "The complete text content to write"}
            },
            "required": ["path", "content"],
            "additionalProperties": False,
        }
        return f"- {self.name}: {self.description}\n  Input schema: {json.dumps(schema, ensure_ascii=False)}"

    def run(self, tool_input: dict) -> dict:
        path = Path(tool_input["path"]).resolve()
        content = str(tool_input["content"])

        # 自动创建不存在的父目录
        path.parent.mkdir(parents=True, exist_ok=True)
        # 写入文件
        path.write_text(content, encoding="utf-8")

        return {"status": f"Successfully wrote {len(content)} characters to {path}"}