package org.obudget.client;

class BudgetLine {
	
	public static final int ALLOCATED = 1;
	public static final int REVISED = 2;
	public static final int USED = 3;
	
	private Integer mNetUsed;
	private Integer mNetRevised;
	private Integer mNetAllocated;
	private Integer mGrossUsed;
	private Integer mGrossRevised;
	private Integer mGrossAllocated;
	private String mTitle;
	private String mCode;
	private Integer mYear;
	private Double mInflation;

	public BudgetLine( String title, 
					   Integer netAllocated,
					   Integer netRevised,
					   Integer netUsed,
					   Integer grossAllocated,
					   Integer grossRevised,
					   Integer grossUsed,
					   String code,
					   Integer year,
					   Double inflation) {
		mTitle = title;
		mNetAllocated = netAllocated;
		mNetRevised = netRevised;
		mNetUsed = netUsed;
		mGrossAllocated = grossAllocated;
		mGrossRevised = grossRevised;
		mGrossUsed = grossUsed;
		mCode = code;
		mYear = year;
		mInflation = inflation;
	}

	public Integer getOriginal( int field, Boolean net ) {
		switch ( field) {
		case ALLOCATED:
			if ( net ) {
				return mNetAllocated;
			} else {
				return mGrossAllocated;
			}
		case REVISED:
			if ( net ) {
				return mNetRevised;
			} else {
				return mGrossRevised;
			}
		case USED:
			if ( net ) {
				return mNetUsed;
			} else {
				return mGrossUsed;
			}
		}
		return null;			
	}

	public Integer getInf( int field, Boolean net ) {
		try {
		switch ( field) {
			case ALLOCATED:
				if ( net ) {
					return (int) (mInflation * mNetAllocated);
				} else {
					return (int) (mInflation * mGrossAllocated);
				}
			case REVISED:
				if ( net ) {
					return (int) (mInflation * mNetRevised);
				} else {
					return (int) (mInflation * mGrossRevised);
				}
			case USED:
				if ( net ) {
					return (int) (mInflation * mNetUsed);
				} else {
					return (int) (mInflation * mGrossUsed);
				}
			}
		} catch (Exception e) {
			return null;						
		}
		return null;			
	}

	public Double getPercent( int field, Boolean net ) {
		try {
			switch ( field) {
				case ALLOCATED:
					if ( net ) {
						return 100.0 * mNetAllocated / TotalBudget.getInstance().getAllocated(mYear,net);
					} else {
						return 100.0 * mGrossAllocated / TotalBudget.getInstance().getAllocated(mYear,net);
					}
				case REVISED:
					if ( net ) {
						return 100.0 * mNetRevised / TotalBudget.getInstance().getRevised(mYear,net);
					} else {
						return 100.0 * mGrossRevised / TotalBudget.getInstance().getRevised(mYear,net);
					}
				case USED:
					if ( net ) {
						return 100.0 * mNetUsed/ TotalBudget.getInstance().getUsed(mYear,net);
					} else {
						return 100.0 * mGrossUsed / TotalBudget.getInstance().getUsed(mYear,net);
					}
				}
			} catch (Exception e) {
				return null;						
			}
			return null;			
	}

	public String getTitle() {
		return mTitle;
	}

	public String getCode() {
		return mCode;
	}

	public Integer getYear() {
		return mYear;
	}
}
