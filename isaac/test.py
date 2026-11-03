import omni.usd

url = omni.usd.get_context().get_stage_url()
print("connected:", url)
with open(r"C:\Users\expo7\isaac_work\result.txt", "w", encoding="utf-8") as f:
    f.write(f"connected: {url}\n")
