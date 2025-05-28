import os
import cairosvg

def convert_svg_to_png():
    # 创建输出文件夹
    output_dir = "converted_pngs"
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历当前目录
    success = 0
    failed = 0
    
    for filename in os.listdir('.'):
        if filename.lower().endswith('.svg'):
            try:
                # 生成输出路径
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_dir, f"{base_name}.png")
                
                # 转换文件
                cairosvg.svg2png(
                    url=filename,
                    write_to=output_path,
                    output_width=1024,  # 可选：设置默认宽度
                    output_height=768   # 可选：设置默认高度
                )
                print(f"✅ 转换成功: {filename} → {output_path}")
                success += 1
            except Exception as e:
                print(f"❌ 转换失败: {filename} - 错误信息: {str(e)}")
                failed += 1
    
    # 输出统计结果
    print(f"\n转换完成！成功 {success} 个，失败 {failed} 个")
    print(f"PNG 文件已保存至: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    convert_svg_to_png()