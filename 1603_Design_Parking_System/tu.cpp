class ParkingSystem {
    vector<int> parking_list;
public:
    ParkingSystem(int big, int medium, int small): parking_list({big, medium, small}) {
    }

    bool addCar(int carType) {
        if(parking_list[carType - 1] == 0)
        {
            return false;
        }
        else
        {
            parking_list[carType - 1]-=1;
            return true;
        }
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */