import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.binary.Hex;

public class fixedxor {
	
	public static String fixedxor(String str1, String str2) throws DecoderException {
		byte[] decoded1 = Hex.decodeHex(str1);
		byte[] decoded2 = Hex.decodeHex(str2);
		StringBuilder result = new StringBuilder();
		
		for (int i = 0; i < decoded1.length; i++) {
			result.append((char)(decoded1[i] ^ decoded2[i]));
		}
		byte[] strbytes = result.toString().getBytes();
		return Hex.encodeHexString(strbytes);
	}
	
	public static void main (String [] args) throws DecoderException {
		String str1 = "1c0111001f010100061a024b53535009181c";
		String str2 = "686974207468652062756c6c277320657965";
		System.out.println(fixedxor(str1, str2));
	}
}
