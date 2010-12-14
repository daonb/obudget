package org.obudget.client;

class BudgetLine {
	private Integer mUsed;
	private Integer mRevised;
	private Integer mAllocated;
	private String mTitle;
	private String mCode;
	private Integer mYear;
	private Double mInflation;

	public BudgetLine( String title, 
					   Integer allocated,
					   Integer revised,
					   Integer used,
					   String code,
					   Integer year,
					   Double inflation) {
		mTitle = title;
		mAllocated = allocated;
		mRevised = revised;
		mUsed = used;
		mCode = code;
		mYear = year;
		mInflation = inflation;
	}

	public Integer getAllocated() {
		return mAllocated;
	}

	public Integer getInfAllocated() {
		return (int) (mInflation * mAllocated);
	}

	public Integer getRevised() {
		return mRevised;
	}

	public Integer getInfRevised() {
		return (int) (mInflation * mRevised);
	}

	public Integer getUsed() {
		return mUsed;
	}

	public Integer getInfUsed() {
		return (int) (mInflation * mUsed);
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
