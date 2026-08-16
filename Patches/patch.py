import os
import sys

def patch_file(filepath, old_text, new_text):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} nahi mila!", file=sys.stderr)
        sys.exit(1)
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if old_text not in content:
        print(f"Warning: Target string not found in {filepath} (Already patched?).")
        return

    content = content.replace(old_text, new_text)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully patched: {filepath}")

def main():
    # Only patching build script now
    build_path = "tdesktop/Telegram/build/build.sh"
    old_build = "./build/docker/centos_env/run.sh /usr/src/tdesktop/Telegram/build/docker/build.sh"
    new_build = """if [ "$BUILD_PART" == "1" ]; then
    echo "Running Build Part 1..."
    ./build/docker/centos_env/run.sh /usr/src/tdesktop/Telegram/build/docker/build.sh --target tgcalls
  else
    echo "Running Build Part 2..."
    ./build/docker/centos_env/run.sh /usr/src/tdesktop/Telegram/build/docker/build.sh
  fi"""
    patch_file(build_path, old_build, new_build)

if __name__ == "__main__":
    main()