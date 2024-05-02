type ParkingSystem struct {
	Hash map[int]int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	hash := map[int]int{
		1: big,
		2: medium,
		3: small,
	}
	return ParkingSystem{
		Hash: hash,
	}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	val := this.Hash[carType]
	if val == 0 {
		return false
	}
	this.Hash[carType]--
	return true
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */
