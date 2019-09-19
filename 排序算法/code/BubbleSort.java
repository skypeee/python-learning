public class BubbleSort {
    public int[] bubbleSort1(int[] arr){
        int length = arr.length;
        if (length == 1){
            return arr;
        }
        for(int i = length ; i >= 0 ; i--){
            for(int j = 0; j < i-1; j++){
                if(arr[j] < arr[j+1]){
                    arr[j] += arr[j+1];
                    arr[j+1] = arr[j] - arr[j+1];
                    arr[j] -= arr[j+1];
                }
            }
        }
        return arr;
    }
    public int[] bubbleSort2(int[] arr){
        int length = arr.length;
        if (length == 1){
            return arr;
        }
        for(int i = length ; i >= 0 ; i--){
            boolean flag = false;
            for(int j = 0; j < i-1; j++){
                if(arr[j] < arr[j+1]){
                    arr[j] += arr[j+1];
                    arr[j+1] = arr[j] - arr[j+1];
                    arr[j] -= arr[j+1];
                    flag = true;
                }
            }
            if(!flag){
                return arr;
            }
        }
        return arr;
    }
    public int[] bubbleSort3(int[] arr){
        int length = arr.length;
        int position = length -1 ;
        int tmpPosition = 0;
        if (length == 1){
            return arr;
        }
        for(int i = length ; i >= 0 ; i--){
            boolean flag = false;
            for(int j = 0; j < position; j++){
                if(arr[j] < arr[j+1]){
                    arr[j] += arr[j+1];
                    arr[j+1] = arr[j] - arr[j+1];
                    arr[j] -= arr[j+1];
                    flag = true;
                    tmpPosition = j;
                }
            }
            position = tmpPosition;
            if(!flag){
                return arr;
            }
        }
        return arr;
    }
    public static void main(String[] args){
        System.out.println("hello");
        BubbleSort b = new BubbleSort();
        int[] a = {7,9,6,8,4,3,2,1};
        int[] x = b.bubbleSort3(a);
        for (int value : x) {
            System.out.println(value);
        }
    }
}
