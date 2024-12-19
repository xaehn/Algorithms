#include <vector>
#include <complex>

using namespace std;
const double _PI = 3.1415926535;
typedef complex<double> cpx;

void DFT(vector<cpx>& v) {
    int _size = v.size(), _corrected_size = 1;
    while (_corrected_size < _size)
        _corrected_size <<= 1;

    v.resize(_corrected_size);
    for (int index = 1, inversed_index = 0; index < _corrected_size; index++) {
        int bit = _corrected_size / 2;
        while (bit <= inversed_index) {
            inversed_index -= bit;
            bit /= 2;
        }

        inversed_index += bit;
        if (index < inversed_index)
            swap(v[index], v[inversed_index]);
    }

    for (int group_size = 1; group_size < _corrected_size; group_size *= 2) {
        cpx unit_per_group(cos(_PI / group_size), -sin(_PI / group_size));
        for (int start_index = 0; start_index < _corrected_size; start_index += 2 * group_size) {
            cpx unit(1, 0);
            for (int index = 0; index < group_size; index++) {
                cpx even = v[start_index + index];
                cpx odd = v[group_size + start_index + index] * unit;

                v[start_index + index] = even + odd;
                v[group_size + start_index + index] = even - odd;

                unit *= unit_per_group;
            }
        }
    }
}