
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

void printLine () {
    string line = "|------------------------------------------------------------------------------------------|";
    // cout << line.length();
    cout << line << endl;
}

void pipe() {
        cout << "|";
}

int getWidth(int val) {
    return 90-(to_string(val).length());
}

int getWidth(string val) {
    return 90-val.length();
}

class Paycheck {
private:
    string firmName;
    int checkNumber;
    string payrollAccount;
    string checkDate;
    string payableTo;
    double grossEarnings;
    string amtAsTxt;
    string companyName;
    string memo;
    string cfo;
public:
    Paycheck(
        string _firmName, 
        int _checkNumber, 
        string _payrollAccount, 
        string _checkDate,
        string _payableTo, 
        double _grossEarnings,
        string _amtAsTxt,
        string _companyName,
        string _memo,
        string _cfo
    ) {
        firmName = _firmName;
        checkNumber = _checkNumber;
        payrollAccount = _payrollAccount;
        checkDate = _checkDate;
        payableTo = _payableTo;
        grossEarnings = _grossEarnings;
        amtAsTxt = _amtAsTxt;
        companyName = _companyName;
        memo = _memo;
        cfo = _cfo;
    }

    void printPaycheck() {
        printLine();
        cout << "|" << setw(getWidth(checkNumber)-8) << left << firmName << right <<"Check #:" << right << checkNumber << "|"<< endl;

        cout << "|" << setw(getWidth(payrollAccount)+1) << left << payrollAccount << right << "Date:" << checkDate << "|" <<endl;

        cout << endl;
        cout << endl; 
        
        cout << "|" << setw(getWidth(payableTo)) << left << "Pay to the order of" << right << payableTo <<"|"<< endl;

        cout << "|" << setw(81) << left << "Date:" << right << checkDate << "|"<<  endl;

        cout << "|" << setw(getWidth(companyName)) << left << companyName << "|"<<  endl;
        cout << "|" << setw(getWidth(memo)) << left << "Memo:" << memo << "|" <<endl;
        cout << "|" << setw(getWidth(cfo)) << left << "Chief Financial Officer" << cfo << "|" << endl; 
        cout << "|" << setw(getWidth(companyName)) << left << "Company Name" << companyName << "|" << endl;
        printLine();
        printLine();
        printLine();
        printLine();
        pipe();
        pipe();
        cout << left << setw(getWidth(grossEarnings)-4) << "Gross earnings:" << "$" << fixed << setprecision(2) << grossEarnings << "|" << endl;
        pipe();
        pipe();
    }
};

// PayStub 
class PayStub {
private:
    string firmName;
    string payrollAccount;
    string checkDate;
    int checkNumber;
    string payableTo;
    string payPeriod;
    double grossEarnings;
    double federalIncomeTax;
    double socialSecurityTax;
    double medicare;
    double stateTax;
    double stateDisabilityInsurance;
    double deductions;
    double netEarnings;
    string memo;
    string cfo;
    string companyName;

public:
    PayStub(string f, string p, string d, int c, string pt, string pp, double g, double fit, double sst, double m, double st, double sdi, string mmo, string co, string cn) {
        firmName = f;
        payrollAccount = p;
        checkDate = d;
        checkNumber = c;
        payableTo = pt;
        payPeriod = pp;
        grossEarnings = g;
        federalIncomeTax = fit;
        socialSecurityTax = sst;
        medicare = m;
        stateTax = st;
        stateDisabilityInsurance = sdi;
        deductions = federalIncomeTax + socialSecurityTax + medicare + stateTax + stateDisabilityInsurance;
        netEarnings = grossEarnings - deductions;
        memo = mmo;
        cfo = co;
        companyName = cn;
    }

    void printPayStub() {
        printLine();
        cout << "|" << setw(79) << left << "Paycheck for" << right << firmName << "|"<< endl;
        cout << "|" << setw(getWidth(payableTo)) << left << "Pay to the order of " << payableTo << "|" <<endl;
        cout << "|" << setw(75) << left << "Account:" << payrollAccount << right << "|"<< endl;
        cout << "|" << setw(81) << left << "Date:" << right << checkDate << "|"<<  endl;
        cout << "|" << setw(87) << left << "Check #:" << right << checkNumber << "|"<<  endl;
        cout << "|" << setw(getWidth(memo)) << left << "Memo:" << memo << "|" <<endl;
        cout << "|" << setw(getWidth(cfo)) << left << "Chief Financial Officer" << cfo << "|" << endl; 
        cout << "|" << setw(getWidth(companyName)) << left << "Company Name" << companyName << "|" << endl;
        printLine();
        printLine();
        printLine();
        printLine();
        pipe();
        cout << left << setw(getWidth(payPeriod)) << "Pay period:" << payPeriod << "|" << endl;
        pipe();
        cout << left << setw(getWidth(grossEarnings)-4) << "Gross earnings:" << "$" << fixed << setprecision(2) << grossEarnings << "|" << endl;
        pipe();
        cout << left << setw(getWidth(federalIncomeTax) - 4) << "Federal income tax:" << "$" << fixed << setprecision(2) <<federalIncomeTax << "|" << endl;
        pipe();
        cout << left << setw(getWidth(socialSecurityTax) - 4) << "Social security tax:" << "$" << fixed << setprecision(2) <<socialSecurityTax << "|" << endl;
        pipe();
        cout << left << setw(getWidth(medicare) - 4) << "Medicare:" << "$" << fixed << setprecision(2) << medicare << "|" << endl;
        pipe();
        cout << left << setw(getWidth(stateTax) - 4) << "State of California tax:" << "$"<< fixed << setprecision(2) <<stateTax << "|" << endl;
        pipe();
        cout << left << setw(getWidth(stateDisabilityInsurance) - 4) << "State disability insurance:" << "$"<< fixed << setprecision(2) <<stateDisabilityInsurance << "|" << endl;
        pipe();
        cout << left << setw(getWidth(deductions) - 4) << "Deductions:" << "$"<< fixed << setprecision(2) <<deductions << "|" << endl;
        pipe();
        cout << left << setw(getWidth(netEarnings) - 4) << "Net earnings:" << "$"<< fixed << setprecision(2) <<netEarnings << "|" << endl;
    }

    double getGrossEarnings() {
        return grossEarnings;
    }

    double getNetEarnings() {
        return netEarnings;
    }

    double getYTPTotalGrossEarnings() {
        return grossEarnings * 26;
    }

    double getYTPTotalNetEarnings() {
        return netEarnings * 26;
    }
};

int main() {
   Paycheck p("ABC VE Firm", 123, "Payroll Account", "10/1/20XX", "Ima Student",1680.0, "One Thousand Six Hundred Eighty Dollars and 0/0 Dollars", "Virtual Enterprises International US Network Banks", "PPF October 31, 20xx", "Cash Isking");

//    PayStub ps("ABC VE Firm", "Payroll Account", "10/1/20XX", 123, "Ima Student",  "10/16/20XX - 10/31/20XX", 1680.0, 141.38, 70.56, 24.36, 23.34, 16.80, "PPF October 31, 20xx", "Cash Isking", "Virtual Enterprises International US Network Banks");

    p.printPaycheck();
    // ps.printPayStub();

    printLine();
    printLine();
    pipe();
    // cout << left << setw(getWidth(p.getGrossEarnings()) - 4) << "Current gross earnings:" << "$" << p.getGrossEarnings() << "|" <<endl;
    // pipe();
    // cout << left << setw(getWidth(p.getNetEarnings()) - 4) << "Current net earnings:" << "$" << p.getNetEarnings() <<"|"<< endl;
    // pipe();
    // cout << left << setw(getWidth(p.getYTPTotalGrossEarnings()) - 4) << "YTP total gross earnings:" << "$" << p.getYTPTotalGrossEarnings() << "|"<<endl;
    // pipe();
    // cout << left << setw(getWidth(p.getYTPTotalNetEarnings()) - 4) << "YTP total net earnings:" << "$" << p.getYTPTotalNetEarnings() <<"|"<< endl;
    // printLine();
    // printLine();
    return 0;
}
