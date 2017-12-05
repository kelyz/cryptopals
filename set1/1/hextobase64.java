import java.util.Base64;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.binary.Hex;

public class hextobase64 {
	
	public static String hextobase64(String s) throws DecoderException {
		byte[] decoded = Hex.decodeHex(s);
		String result = Base64.getEncoder().encodeToString(decoded);
		return result;
	}
	
	public static void main (String [] args) throws DecoderException {
		String test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
		System.out.println(hextobase64(test));
	}
}
