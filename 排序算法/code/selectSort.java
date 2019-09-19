public class selectSort {
    public int[] sort(int[] arr){
        int lenth = arr.length;
        for(int i=0;i<lenth;i++){
            int minIndex = i;
            for(int j=i+1;j<lenth;j++){
                if(arr[minIndex] > arr[j]){
                    minIndex = j;
                }
            }
            int tmp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = tmp;
        }
        return arr;
    }
    public static void main(String[] args){
        selectSort a = new selectSort();
        int[] b = {2,3,8,5,3,1,4,6,7};
        int[] x = a.sort(b);
        for(int i=0;i<x.length;i++){
            System.out.println(b[i]);
        }
    }
}
