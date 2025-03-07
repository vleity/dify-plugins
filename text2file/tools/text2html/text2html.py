from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import mimetypes

class Text2htmlTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        text = tool_parameters.get("text","")
        filename = tool_parameters.get("filename","")
        mime_type,_ = mimetypes.guess_type(filename)
        file_bytes = text.encode(encoding="utf-8")
        meta = {
            "filename": filename,
            "mime_type": mime_type
        }
        yield self.create_json_message(
            json = {
                "text": text,
                "filename": filename
            }
        )
        yield self.create_blob_message(
            blob = file_bytes,
            meta = meta
        )
        yield self.create_text_message(
            text = text
        )
