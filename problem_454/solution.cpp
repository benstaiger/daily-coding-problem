#include <algorithm>
#include <chrono>
#include <iostream>
#include <numeric>  // std::accumulate
#include <tuple>
#include <vector>

// This problem was asked by Dropbox.
//
// Conway's Game of Life takes place on an infinite two-dimensional board of
// square cells. Each cell is either dead or alive, and at each tick, the
// following rules apply:
//
// Any live cell with less than two live neighbours dies.
// Any live cell with two or three live neighbours remains living.
// Any live cell with more than three live neighbours dies.
// Any dead cell with exactly three live neighbours becomes a live cell.
// A cell neighbours another cell if it is horizontally, vertically, or
// diagonally adjacent.
//
// Implement Conway's Game of Life. It should be able to be initialized with
// a starting list of live cell coordinates and the number of steps it should
// run for. Once initialized, it should print out the board state at each
// step. Since it's an infinite board, print out only the relevant
// coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live
// cell.
//
// You can represent a live cell with an asterisk (*) and a dead cell with a
// dot (.).

// In a real solution, one should probably use a Dense/Sparse type from an
// existing library, Eigen, etc.

using Index = std::pair<int, int>;
using Quadple = std::tuple<int, int, int, int>;

namespace {

Quadple boundsUpdate(const Quadple &current, const Index &next) {
  return {std::min(std::get<0>(current), next.first),
          std::max(std::get<1>(current), next.first),
          std::min(std::get<2>(current), next.second),
          std::max(std::get<3>(current), next.second)};
}

Quadple bounds(const std::vector<Index> &values) {
  return std::accumulate(
      values.begin(), values.end(),
      Quadple(std::numeric_limits<int>::max(), std::numeric_limits<int>::min(),
              std::numeric_limits<int>::max(), std::numeric_limits<int>::min()),
      boundsUpdate);
}

}  // namespace

template <typename T>
class DenseMat {
 public:
  DenseMat() : _defaultVal(T()), _rows(0), _cols(0), _data() {}
  DenseMat(int rows, int cols, T defaultVal)
      : _defaultVal(defaultVal),
        _rows(rows),
        _cols(cols),
        _data(rows * cols, defaultVal) {}
  T at(int i, int j) const {
    if (!(i >= 0 && i < _rows && j >= 0 && j < _cols)) return _defaultVal;
    return _data[i * _cols + j];
  }
  DenseMat<T> Slice(int startRow, int endRow, int startCol, int endCol) const {
    DenseMat<T> res(endRow - startRow + 1, endCol - startCol + 1, _defaultVal);
    for (int i = 0; i < res.Rows(); ++i) {
      for (int j = 0; j < res.Cols(); ++j) {
        res(i, j) = this->at(startRow + i, startCol + j);
      }
    }
    return res;
  }
  T &operator()(int i, int j) {
    if (!(i >= 0 && i < _rows && j >= 0 && j < _cols))
      throw std::invalid_argument("Index out of bounds.");
    return _data[i * _cols + j];
  }
  const T &operator()(int i, int j) const {
    if (!(i >= 0 && i < _rows && j >= 0 && j < _cols))
      throw std::invalid_argument("Index out of bounds.");
    return _data[i * _cols + j];
  }
  int Rows() { return _rows; }
  int Cols() { return _cols; }

 private:
  T _defaultVal;
  int _rows;
  int _cols;
  std::vector<T> _data;
};

template <class Storage>
class GameOfLife {
 public:
  GameOfLife(const std::vector<Index> &initialState, size_t cycles)
      : _cycles(cycles) {
    const auto [minRow, maxRow, minCol, maxCol] = bounds(initialState);
    _live = Storage(maxRow - minRow + 1, maxCol - minCol + 1, '.');
    for (const auto [row, col] : initialState) {
      _live(row - minRow, col - minCol) = '*';
    }
  }
  void Run() {
    for (size_t i = 0; i <= _cycles; ++i) {
      std::cout << "Itr: " << i << std::endl;
      Print();
      Step();
    }
  }
  void Step() {
    Storage nextItr(_live.Rows() + 2, _live.Cols() + 2, '.');
    Quadple extrema{nextItr.Rows(), 0, nextItr.Cols(), 0};

    // for each position, check if it should be alive.
    for (size_t i = 0; i < nextItr.Rows(); ++i) {
      for (size_t j = 0; j < nextItr.Cols(); ++j) {
        const int adjacent = CheckAdjacent(i - 1, j - 1);
        const bool currentlyAlive = _live.at(i - 1, j - 1) == '*';
        if (adjacent == 3 || adjacent == 2 && currentlyAlive) {
          nextItr(i, j) = '*';
          extrema = boundsUpdate(extrema, {i, j});
        }
      }
    }
    const auto [minRow, maxRow, minCol, maxCol] = extrema;
    _live = nextItr.Slice(minRow, maxRow, minCol, maxCol);
  }
  void Print() {
    for (int i = 0; i < _live.Rows(); ++i) {
      for (int j = 0; j < _live.Cols(); ++j) {
        std::cout << _live(i, j);
      }
      std::cout << std::endl;
    }
  }

 private:
  int CheckAdjacent(int row, int col) {
    int adj = 0;
    for (int i = -1; i <= 1; ++i) {
      for (int j = -1; j <= 1; ++j) {
        if (i == 0 && j == 0) continue;
        if (_live.at(row + i, col + j) == '*') {
          ++adj;
        }
      }
    }
    return adj;
  }

  const size_t _cycles;
  Storage _live;
};

int main() {
  GameOfLife<DenseMat<char>> example({{{1, 1}, {1, 2}, {1, 3}, {2, 1}}}, 5);
  example.Run();
}