public class insertionSort {
    public  int[] Sort(int[] arr){
        int lenth = arr.length;
        for(int i=1; i < lenth; i++){
            int key = arr[i];
            int j = i-1;
            while(j>=0 && key<= arr[j]){
                arr[j+1] =arr[j];
                j -= 1;
            }
            arr[j+1] = key;
        }
        return arr;
    }
    public static void main(String[] args){
        insertionSort a = new insertionSort();
        int[] x = {2,8,1,6,8,4,2,6,8,9};
        int []result = a.Sort(x);
        for(int i=0;i<result.length;i++){
            System.out.println(result[i]);
        }

    }
}
