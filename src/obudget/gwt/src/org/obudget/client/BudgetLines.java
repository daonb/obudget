package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.json.client.JSONObject;

class BudgetLines extends LinkedList<BudgetLine> {
	/**
	 * 
	 */
	private static final long serialVersionUID = 6274721656454210674L;

	public void parseJson( JSONArray data ) {
		clear();
		for ( int i = 0 ; i < data.size() ; i ++ ) {
			JSONObject obj = data.get(i).isObject();
			BudgetLine bl = new BudgetLine( obj.get("title").isString().stringValue(), 
											(int) obj.get("amount_allocated").isNumber().doubleValue(), 
											(int) obj.get("amount_revised").isNumber().doubleValue(), 
											(int) obj.get("amount_used").isNumber().doubleValue(),
											obj.get("budget_id").isString().stringValue(), 
											(int) obj.get("year").isNumber().doubleValue(),
											obj.get("inflation_factor").isNumber().doubleValue() );
			addLast(bl);
		}		
	}
}

