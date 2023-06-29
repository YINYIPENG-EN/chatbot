import speech_recognition as sr
import pyaudio, wave

def Speech_Recognition(audio_file='voice.wav'):
    # 创建语音识别器
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
    # 音频转文字
    text = r.recognize_google(audio_data, language='zh-CN')
    #print(text)
    return text

# 录制wav
def save_wav(out_file='voice.wav', rec_time=5):
    pa = pyaudio.PyAudio()

    # 设置声卡参数
    chunk = 1024  # 帧长度
    Format = pyaudio.paInt16  # 采样深度
    CHANNELS = 2  # 声道
    RATE = 16000  # 采样率
    record_seconds = rec_time  # 设置录制时间
    # RATE/chunk*record_seconds为一秒采样数除以一帧长度和录制秒数可以得到帧数

    # 新建一个列表，用来存储数据
    record_list = []

    # 打开声卡，设置参数,设置音频流
    stream = pa.open(format=Format, rate=RATE, channels=CHANNELS, frames_per_buffer=chunk, input=True)

    # 开始录制
    print('开始录制...')

    # 进行录制与采样
    for i in range(0, int(RATE / chunk * record_seconds)):
        data = stream.read(chunk)  # 为每一帧的样本二进制数据
        record_list.append(data)  # 得到的是保存的二进制数据

    # 录制完成
    stream.stop_stream()  # 停止调用声卡
    stream.close()  # 关闭声卡
    pa.terminate()  # 结束pyaudio对象
    print('录制结束...')

    # 保存音频文件（wav文件类型）
    file = wave.open(out_file, 'wb')  # 创建voice文件
    file.setnchannels(CHANNELS)  # 设置声道数
    file.setsampwidth(pa.get_sample_size(Format))  # 设置采样宽度，通过pa.get_sample_size(format)可以得到
    file.setframerate(RATE)  # 设置采样率
    file.writeframes(b''.join(record_list))  # 将二进制文件加入到wav文件之中
    file.close()




