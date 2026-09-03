from client import RealtimeAudioDiarizationSpeakerAssignerClient

def main():
    client = RealtimeAudioDiarizationSpeakerAssignerClient()
    res = client.diarize_audio_channel('audio_bytes', ['David (Lead Dev)', 'Emma (Designer)'])
    print('Audio Diarization Speaker Assigner: ' + res['diarization_event_id'] + ' (' + res['identified_speaker_id'] + ')')
    print('Speech: "' + res['transcribed_speech_text'] + '" (Confidence: ' + str(res['speaker_embedding_similarity']) + ')')
    print('Timeline URL: ' + res['multi_speaker_timeline_url'])

if __name__ == '__main__':
    main()
