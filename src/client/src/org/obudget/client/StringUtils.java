package org.obudget.client;

public class StringUtils {

	public static native String getUserAgent() /*-{
 		return navigator.userAgent.toLowerCase();
	}-*/;

	public static String compStr( String input ) {
		if ( getUserAgent().contains("firefox/3") ) {
			String out = "";
			for ( int i = input.length() ; i --> 0 ; ) {
				out += input.charAt(i);
			}
			return out;
		} else {
			return input;
		}
	}
}
