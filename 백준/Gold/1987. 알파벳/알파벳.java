import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int R, C;
	static char[][] arr;
	static boolean[] visited = new boolean[26]; // 각 알파벳을 방문했는지 확인하는 배열
	static int[][] count;
	static int[] dr = { -1, 0, 1, 0 };
	static int[] dc = { 0, 1, 0, -1 };
	static int ans = 0;
	static int result = 0;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken()); // 1 <= R, C <= 20
		arr = new char[R][];
		count = new int[R][C];

		for (int i = 0; i < R; i++) {
			String str = br.readLine();
			arr[i] = str.toCharArray();
		}

		dfs2(0, 0, 1);
//		for (int i = 0; i < R; i++) {
//			for (int j = 0; j < C; j++) {
//				if (count[i][j] > ans)
//					ans = count[i][j];
//			}
//		}
		System.out.println(result);
//		for(int i = 0; i < R; i++) {
//			System.out.println(Arrays.toString(count[i]));
//		}

	} // end of main

	public static void dfs(int r, int c, int num) {
		visited[arr[r][c] - 'A'] = true;
		count[r][c] = num + 1;

		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];

			if (0 <= nr && nr < R && 0 <= nc && nc < C) {
				if (!visited[arr[nr][nc] - 'A']) {
					dfs(nr, nc, count[r][c]);
				}
			}
		}
		visited[arr[r][c] - 'A'] = false;

	}

	public static void dfs2(int r, int c, int cnt) {
		visited[arr[r][c] - 'A'] = true;
		result = Math.max(cnt, result);

		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];

			if (0 <= nr && nr < R && 0 <= nc && nc < C) {
				if (!visited[arr[nr][nc] - 'A']) {
					dfs2(nr, nc, cnt + 1);
				}
			}
		}
		visited[arr[r][c] - 'A'] = false;

	}
} // end of class
