package org.obudget.client;

import java.util.HashMap;

import com.google.gwt.json.client.JSONArray;

public class TotalBudget {

	BudgetLines mBudgetLines = new BudgetLines();
	HashMap<Integer, Integer> totalAllocatedNet = new HashMap<Integer, Integer>(); 
	HashMap<Integer, Integer> totalRevisedNet = new HashMap<Integer, Integer>(); 
	HashMap<Integer, Integer> totalUsedNet = new HashMap<Integer, Integer>(); 
	HashMap<Integer, Integer> totalAllocatedGross = new HashMap<Integer, Integer>(); 
	HashMap<Integer, Integer> totalRevisedGross = new HashMap<Integer, Integer>(); 
	HashMap<Integer, Integer> totalUsedGross = new HashMap<Integer, Integer>(); 
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
					totalAllocatedNet.put(bl.getYear(), bl.getOriginal( BudgetLine.ALLOCATED, true ));
					totalRevisedNet.put(bl.getYear(), bl.getOriginal( BudgetLine.REVISED, true ));
					totalUsedNet.put(bl.getYear(), bl.getOriginal( BudgetLine.USED, true ));
					totalAllocatedGross.put(bl.getYear(), bl.getOriginal( BudgetLine.ALLOCATED, false ));
					totalRevisedGross.put(bl.getYear(), bl.getOriginal( BudgetLine.REVISED, false ));
					totalUsedGross.put(bl.getYear(), bl.getOriginal( BudgetLine.USED, false ));
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
	
	public Integer getAllocated( Integer year, Boolean net ) {
		if ( net ) {
			return totalAllocatedNet.get(year);
		} else {
			return totalAllocatedGross.get(year);			
		}
	}

	public Integer getRevised( Integer year, Boolean net ) {
		if ( net ) {
			return totalRevisedNet.get(year);
		} else {
			return totalRevisedGross.get(year);			
		}
	}

	public Integer getUsed( Integer year, Boolean net ) {
		if ( net ) {
			return totalUsedNet.get(year);
		} else {
			return totalUsedGross.get(year);			
		}
	}
}
