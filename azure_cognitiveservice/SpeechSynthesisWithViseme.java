import com.microsoft.cognitiveservices.speech.*;
import com.microsoft.cognitiveservices.speech.audio.*;
import java.util.concurrent.ExecutionException;

public class SpeechSynthesisWithViseme {
    public static void main(String[] args) {
        try {
            // Replace with your own subscription key and region
            String subscriptionKey = "1a37c2b2c1ad42af93fc80fce6bb38fb";
            String region = "eastus";

            // Replace with your own SSML string
            String ssml = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' "
                + "xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='en-US'>"
                + "<voice name='en-US-AriaNeural'>"
                + "<mstts:viseme  type=\"FacialExpression\" time='500'/>Hello<mstts:viseme  type=\"FacialExpression\" time='1000'/>world"
                + "</voice></speak>";

            // Creates an instance of a speech synthesizer
            SpeechConfig speechConfig = SpeechConfig.fromSubscription(subscriptionKey, region);
            AudioConfig audioConfig = AudioConfig.fromDefaultSpeakerOutput();
            SpeechSynthesizer synthesizer = new SpeechSynthesizer(speechConfig, audioConfig);

            // Subscribes to viseme received event
            synthesizer.VisemeReceived.addEventListener((o, e) -> {
                // The unit of e.AudioOffset is tick (1 tick = 100 nanoseconds), divide by 10,000 to convert to milliseconds.
                // System.out.print("Viseme event received. Audio offset: " + e.getAudioOffset() / 10000 + "ms, ");
                // System.out.println("viseme id: " + e.getVisemeId() + ".");

                // `Animation` is an xml string for SVG or a json string for blend shapes
                String animation = e.getAnimation();
                if (animation != null) {
                    System.out.println("Animation string: " + animation);
                }
            });

            // Synthesizes speech and waits for the result
            SpeechSynthesisResult result = synthesizer.SpeakSsmlAsync(ssml).get();

            // Checks the result
            if (result.getReason() == ResultReason.SynthesizingAudioCompleted) {
                System.out.println("Speech synthesis succeeded.");
            } else if (result.getReason() == ResultReason.Canceled) {
                SpeechSynthesisCancellationDetails cancellation = SpeechSynthesisCancellationDetails.fromResult(result);
                System.out.println("Speech synthesis canceled. Reason: " + cancellation.getReason() + ". Error code: " + cancellation.getErrorCode());
            } else {
                System.out.println("Speech synthesis failed. Reason: " + result.getReason());
            }

            // Cleans up resources
            synthesizer.close();
            audioConfig.close();
            speechConfig.close();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}