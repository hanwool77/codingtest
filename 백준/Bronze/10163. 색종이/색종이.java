import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine()); // 색종이의 수
		int[][] arr = new int[101][101];

		for (int i = 1; i <= N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken()); // 색종이 가로 길이
			int h = Integer.parseInt(st.nextToken()); // 색종이 세로 길이

			for (int r = x; r < x + w; r++) {
				for (int c = y; c < y + h; c++) {
					arr[r][c] = i;
				}
			}
		}
		int[] answer = new int[N + 1];
		for (int i = 0; i < 101; i++) {
			for (int j = 0; j < 101; j++) {
				if (arr[i][j] != 0) {
					answer[arr[i][j]]++;
				}
			}
		}
		for(int i = 1; i <= N; i++) {
			System.out.println(answer[i]);
		}
	}
}
