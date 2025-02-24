from moviepy.editor import ImageClip, concatenate_videoclips, vfx

# 加载图片
clip_a = ImageClip("a.png").set_duration(2)  # a 图片显示2秒
clip_b = ImageClip("b.png").set_duration(2)  # b 图片显示2秒

# 创建过渡效果
transition = clip_a.crossfadeout(1).set_duration(1)  # 1秒的过渡效果

# 将所有片段连接在一起
final_clip = concatenate_videoclips([clip_a, transition, clip_b], method="compose")

# 导出视频
final_clip.write_videofile("output_video.mp4", fps=24)
