from moviepy.editor import VideoFileClip

# 定义要提取帧的时间点（以秒为单位）
times_to_capture = [2, 6, 10, 14]

# 加载视频
video = VideoFileClip("your_video.mp4")

# 遍历每个时间点并保存帧
for time in times_to_capture:
    # 获取特定时间点的帧
    frame = video.get_frame(time)
    
    # 保存帧为PNG文件
    frame_filename = f"frame_at_{time}s.png"
    frame_image = Image.fromarray(frame)
    frame_image.save(frame_filename)

print("帧提取完成！")
