# Binary Search and Merge Sort Performance Analysis

This Python project implements two classic algorithms — *Binary Search* and *Merge Sort* — and evaluates their performance using different datasets. The goal is to observe how each algorithm behaves under sorted, reversed, and random data conditions.

## 🔍 Algorithms Implemented

### 1. Binary Search
A fast search algorithm that works on sorted lists by repeatedly dividing the search interval in half.

### 2. Merge Sort
A divide-and-conquer sorting algorithm with guaranteed O(n log n) time complexity in all cases.

---

## 📊 Features

- Performance analysis with:
  - *Time tracking* using time.perf_counter()
  - *Memory usage* tracking with tracemalloc
- Testing on three types of datasets:
  - Sorted
  - Reversed
  - Random
- Readable and modular code structure

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.x installed.

### Installation and Execution

Clone the repository:

```bash
git clone https://github.com/Sahithibontha515/MSCS532_Assignment2
cd MSCS532_Assignment2

python run BinarySearch.py 
pythin run MergeSort.py

