import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

async def main():
    async with client:
        result = await client.call_tool("get_github_issues", {"repo_name": "smatz-ITGAIN/mcp-demo"})
        print("------------------------------")
        print(f"Full call result:\n{result}")
        print("------------------------------")
        print(f"Just result:\n{result.data}")

asyncio.run(main())
