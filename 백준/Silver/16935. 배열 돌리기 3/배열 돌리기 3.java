import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int R;
	static int[][] arr;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken()); // 2 <= N <= 100
		M = Integer.parseInt(st.nextToken()); // 2 <= M <= 100
		R = Integer.parseInt(st.nextToken()); // 1 <= R <= 1000

		arr = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int x[] = new int[R];
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < R; i++) {
			x[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 0; i < R; i++) {
			switch (x[i]) {
			case 1: // 상하 반전
				func1();
				break;
			case 2: // 좌우 반전
				func2();
				break;

			case 3: // 우측 90도 회전
				func3();
				break;

			case 4: // 좌측 90도 회전
				func4();
				break;
			case 5:
				func5();
				break;

			case 6:
				func6();
				break;
			} // end of switch

		}

		// 출력
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				sb.append(arr[i][j]).append(" ");
			}
			sb.append("\n");
		}

		System.out.println(sb.toString());
	} // end of main

	// 상하 반전
	private static void func1() {
		int[][] temp = new int[N][M];
		for (int i = 0; i < N; i++) {
			temp[i] = arr[N - i - 1];
		}
		arr = temp;
	}

	// 2번 좌우 반전
	private static void func2() {
		int[][] temp = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				temp[i][j] = arr[i][M - j - 1];
			}
		}
		arr = temp;
	}

	// 3번 우측 90도 회전
	private static void func3() {
		int[][] temp = new int[M][N];
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				temp[i][j] = arr[N - j - 1][i];
			}
		}
		arr = temp;
		int tmp = N;
		N = M;
		M = tmp;
	}

	// 4번 좌측 90도 회전
	private static void func4() {
		int[][] temp = new int[M][N];
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				temp[i][j] = arr[j][M - i - 1];
			}
		}
		arr = temp;
		int tmp = N;
		N = M;
		M = tmp;
	}

	// 5번 연산
	private static void func5() {
		int[][] temp = new int[N][M];
		int hN = N / 2;
		int hM = M / 2;

		for (int i = 0; i < hN; i++) {
			for (int j = 0; j < hM; j++) {
				temp[i][j + hM] = arr[i][j]; // 1 -> 2
				temp[i + hN][j + hM] = arr[i][j + hM]; // 2 -> 3
				temp[i + hN][j] = arr[i + hN][j + hM]; // 3 -> 4
				temp[i][j] = arr[i + hN][j]; // 4 -> 1
			}
		}
		arr = temp;
	}

	// 6번 연산
	private static void func6() {
		int[][] temp = new int[N][M];
		int hN = N / 2;
		int hM = M / 2;

		for (int i = 0; i < hN; i++) {
			for (int j = 0; j < hM; j++) {
				temp[i][j] = arr[i][j + hM]; // 2 -> 1
				temp[i][j + hM] = arr[i + hN][j + hM]; // 3 -> 2
				temp[i + hN][j + hM] = arr[i + hN][j]; // 4- > 3
				temp[i + hN][j] = arr[i][j]; // 1 -> 4
			}
		}
		arr = temp;
	}
} // end of class
