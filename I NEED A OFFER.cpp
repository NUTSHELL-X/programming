#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

float least_one_offer(vector<int> price, vector<float> possibility,int money) {
	//dp[i+1][j]=min(dp[i][j],dp[i][j-price[i]]*(1.0-possibility[i]))
	vector<vector<float>> dp;
	for (int i = 0; i <= price.size(); i++) {
		vector<float> temp;
		for (int j = 0; j <= money; j++) {
			temp.push_back(1.0);
		}
		dp.push_back(temp);
	}
	for (int i = 0; i < price.size(); i++) {
		for (int j = 0; j <= money; j++) {
			if (j - price[i] >= 0) {
				dp[i + 1][j] = min(dp[i][j], float(dp[i][j - price[i]] * (1.0 - possibility[i])));
			}
			else {
				dp[i + 1][j] = dp[i][j];
			}
		}
	}
	//cout<<dp[price.size()][money];
	return 1.0-dp[price.size()][money];
}
int main() {
	int money = 0;
	int n = 0;
	int price_temp = 0;
	float possibility_temp = 0.0;
	vector<int> price;
	vector<float> possibility;
	while(1){
		cin >> money;
		cin >> n;
		if (money == 0 && n == 0) break;
		for (int i = 0; i < n; i++) {
			cin >> price_temp;
			cin >> possibility_temp;
			price.push_back(price_temp);
			possibility.push_back(possibility_temp);
		}
		float ans = least_one_offer(price, possibility, money);
		if (n == 0) ans = 0.0;
		printf("%0.1f", 100 * ans);
		printf("%%");
		cout << endl;
		price.clear();
		possibility.clear();
	}	
	return 0;
}
