import os
import cairosvg

def convert_svg_to_png():
    # 创建输出文件夹
    output_dir = "converted_pngs"
    os.makedirs(output_dir, exist_ok=True)
    
    success = 0
    failed = 0
    
    for filename in os.listdir('.'):
        if filename.lower().endswith('.svg'):
            try:
                # 读取 SVG 内容
                with open(filename, "r", encoding="utf-8") as f:
                    svg_data = f.read()
                
                # 替换填充颜色
                #svg_data = svg_data.replace('fill="currentColor"', 'fill="#888888"')
                svg_data = svg_data.replace('fill:#000', 'fill:#00000')  # 处理样式内填色

                # 输出 PNG 路径
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_dir, f"{base_name}.png")

                # 转换为 PNG
                cairosvg.svg2png(
                    bytestring=svg_data.encode('utf-8'),
                    write_to=output_path,
                    output_width=128,
                    output_height=128
                )
                print(f"✅ 转换成功: {filename} → {output_path}")
                success += 1
            except Exception as e:
                print(f"❌ 转换失败: {filename} - 错误信息: {str(e)}")
                failed += 1

    # 输出结果
    print(f"\n转换完成！成功 {success} 个，失败 {failed} 个")
    print(f"PNG 文件保存在: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    convert_svg_to_png()
