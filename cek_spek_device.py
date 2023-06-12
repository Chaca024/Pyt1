import platform
print("===============================================")
print("system information")
print("===============================================")
sys = platform.uname()

print(f"node name  :{sys.node}")
print(f"system     :{sys.system}")
print(f"release    :{sys.release}")
print(f"version    :{sys.version}")
print(f"machine    :{sys.machine}")
print(f"processor  :{sys.processor}")

print("==============================================")