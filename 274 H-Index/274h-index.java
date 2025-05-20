class Solution {
    public void heapify(int arr[], int n, int i) {

            // Initialize largest as root
            int largest = i; 

            // left index = 2*i + 1
            int l = 2 * i + 1; 

            // right index = 2*i + 2
            int r = 2 * i + 2;

            // If left child is larger than root
            if (l < n && arr[l] > arr[largest]) {
                largest = l;
            }

            // If right child is larger than largest so far
            if (r < n && arr[r] > arr[largest]) {
                largest = r;
            }

            // If largest is not root
            if (largest != i) {
                int temp = arr[i];
                arr[i] = arr[largest];
                arr[largest] = temp;

                // Recursively heapify the affected sub-tree
                heapify(arr, n, largest);
            }
        }

        public void heapSort(int arr[]) {
            int n = arr.length;

            // Build heap (rearrange array)
            for (int i = n / 2 - 1; i >= 0; i--) {
                heapify(arr, n, i);
            }

            // One by one extract an element from heap
            for (int i = n - 1; i > 0; i--) {

                // Move current root to end
                int temp = arr[0]; 
                arr[0] = arr[i];
                arr[i] = temp;

                // Call max heapify on the reduced heap
                heapify(arr, i, 0);
            }
        }

    public int hIndex(int[] citations) {
        /*
        for (int i = 1; i<citations.length; i++){
            int key = citations[i];
            int j = i-1;
            while ( j >= 0 && citations[j]>key){
                citations[j+1] = citations[j];
                j--;
            }
            citations[j + 1] = key;
        }
        */

        heapSort(citations);

        int len = citations.length;
        int n = citations.length-1;
        int best = 0;
        while ( n >= 0  ){
            int difference = len - n;
            if (citations[n] >= difference){
                best = Math.max(best,difference );
            }
            n--;
        }
        return best;
    }

    
}