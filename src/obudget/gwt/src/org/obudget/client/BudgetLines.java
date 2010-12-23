package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.json.client.JSONObject;

class BudgetLines extends LinkedList<BudgetLine> {
	/**
	 * 
	 */
	private static final long serialVersionUID = 6274721656454210674L;

	private Integer getInt( JSONObject obj, String fieldname ) {
		if (obj.get(fieldname) == null ) return null;
		if (obj.get(fieldname).isNumber() == null ) return null;
		return (int) obj.get(fieldname).isNumber().doubleValue(); 
	}
	
	public void parseJson( JSONArray data ) {
		clear();
		for ( int i = 0 ; i < data.size() ; i ++ ) {
			JSONObject obj = data.get(i).isObject();
			BudgetLine bl = new BudgetLine( obj.get("title").isString().stringValue(), 
											getInt(obj,"net_amount_allocated"), 
											getInt(obj,"net_amount_revised"), 
											getInt(obj,"net_amount_used"),
											getInt(obj,"gross_amount_allocated"), 
											getInt(obj,"gross_amount_revised"), 
											getInt(obj,"gross_amount_used"),
											obj.get("budget_id").isString().stringValue(), 
											getInt(obj,"year"),
											obj.get("inflation_factor").isNumber().doubleValue() );
			addLast(bl);
		}		
	}
}

