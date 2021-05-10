```python
def listen_print_loop(responses):
    """서버 응답을 반복하고 출력합니다.
    전달된 응답은 응답이 발생할 때까지 차단되는 생성기입니다.
    서버에서 제공합니다.
    각 응답에는 여러 결과가 포함될 수 있으며 각 결과에는
    여러 대안; 자세한 내용은 https://goo.gl/tjCPAU를 참조하세요. 여기 우리
    상위 결과의 상위 대안에 대한 트랜스크립션만 인쇄합니다.
    이 경우 중간 결과에 대한 응답도 제공됩니다. 만약
    응답은 중간 응답입니다. 마지막에 줄 바꿈을 인쇄하여
    응답이 최종 결과가 될 때까지 덮어 쓸 다음 결과. 에 대한
    마지막으로, 최종 전사를 보존하기 위해 개행을 인쇄하십시오.
    """
    num_chars_printed = 0
    for  response  in  responses :
        if not response.results:
            continue

		#`results` 목록은 연속적입니다. 스트리밍의 경우 우리는
        # 고려되는 첫 번째 결과, 일단`is_final`이되면
        # 다음 발화 고려로 이동합니다.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

	   # 중간 결과를 표시하지만 끝에 캐리지 리턴이 있습니다.
        # 줄이므로 다음 줄이 덮어 씁니다.
        #
        # 이전 결과가이 결과보다 길면 인쇄해야합니다.
        # 이전 결과를 덮어 쓸 추가 공백
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + '\r')
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('Exiting..')
                break

            num_chars_printed = 0





        # +
        if (transcript + overwrite_chars) == "ok"  or  (transcript + overwrite_chars) == "okay"  or  (transcript + overwrite_chars) == " ok"  or  (transcript + overwrite_chars) == " okay":
            print("WOW")
            #pyautogui.doubleClick()
            pyautogui . click ()
        elif (transcript + overwrite_chars) == "no"  or  (transcript + overwrite_chars) == " no":
            print("RightMouseClick")
            pyautogui.rightClick()








        


def Audio_main():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = 'en-US'  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for  content  in  audio_generator )

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses)


```

- 구글 서버를 통해 인식된 결과가 transcript + overwrite_chars 변수에 받아진다.

  이를 문자열과 대조해 상황에 맞는 응답을 출력하였다.

- 클라이언트, 서버 요청 및 응답에 관한 코드가 있다. -서버응답!