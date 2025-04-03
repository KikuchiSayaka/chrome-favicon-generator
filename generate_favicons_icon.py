# Chrome拡張機能用のファビコンを生成するスクリプト
# 画像を指定されたサイズにリサイズし、PNG形式で保存します。
from PIL import Image
import os

# ダウンロードフォルダのパス（Windows / macOS / Linux に対応）
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")


def generate_favicons(input_image_path):
    # ダウンロードフォルダ + 入力されたパスを結合
    full_image_path = os.path.join(download_folder, input_image_path)

    # 出力ファイルのサイズと名前のマッピング
    sizes = {
        "favicon16x16.png": (16, 16),
        "favicon32x32.png": (32, 32),
        "favicon48x48.png": (48, 48),
        "favicon128x128.png": (128, 128),
    }

    # 画像を開く
    try:
        img = Image.open(full_image_path)
    except Exception as e:
        print(f"[ERROR] 画像を開けませんでした: {e}")
        return

    # 出力ディレクトリ（ダウンロードフォルダに保存）
    output_dir = download_folder

    for filename, size in sizes.items():
        resized_img = img.resize(size, Image.LANCZOS)
        output_path = os.path.join(output_dir, filename)
        resized_img.save(output_path, format="PNG")
        print(f"生成完了: {output_path}")


# 実行
if __name__ == "__main__":
    input_image_path = input(
        "変換元になる画像のファイル名を入力してください（例: sample.jpg）: "
    ).strip()
    generate_favicons(input_image_path)
