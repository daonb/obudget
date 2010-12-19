package org.obudget.client;

import java.util.HashMap;

import com.google.gwt.json.client.JSONArray;

public class TotalBudget {

	BudgetLines mBudgetLines = new BudgetLines();
	HashMap<Integer, Integer> totalAllocated = new HashMap<Integer, Integer>(); 
	HashMap<Integer, Integer> totalRevised = new HashMap<Integer, Integer>(); 
	HashMap<Integer, Integer> totalUsed = new HashMap<Integer, Integer>(); 
	static TotalBudget mInstance = null;
	
	private TotalBudget() {
		BudgetAPICaller totalBudget = new BudgetAPICaller();
		totalBudget.setCode("00");
		totalBudget.setParameter("depth", "0");
		totalBudget.go( new BudgetAPICallback() {		
			@Override
			public void onSuccess(JSONArray data) {
				mBudgetLines.parseJson(data);
				for ( BudgetLine bl : mBudgetLines ) {
					totalAllocated.put(bl.getYear(), bl.getAllocated());
					totalRevised.put(bl.getYear(), bl.getRevised());
					totalUsed.put(bl.getYear(), bl.getUsed());
				}
			}
		});
	}
	
	static public TotalBudget getInstance() {
		if ( mInstance == null ) {
			mInstance = new TotalBudget();
		}
		return mInstance;
	}
	
	public Integer getAllocated( Integer year ) {
		return totalAllocated.get(year);
	}

	public Integer getRevised( Integer year ) {
		return totalRevised.get(year);
	}

	public Integer getUsed( Integer year ) {
		return totalUsed.get(year);
	}
}
