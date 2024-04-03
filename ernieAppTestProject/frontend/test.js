
const { displayBusDetailsAndSeats, resetReservationForm } = require('./your-file-name');

// Mock the document.getElementById function
document.getElementById = jest.fn(id => {
    return {
        value: '',
        disabled: false,
        textContent: '',
        style: { display: '' },
        innerHTML: ''
    };
});

// Mock the document.getElementsByClassName function
document.getElementsByClassName = jest.fn(className => {
    return [{
        style: { display: '' }
    }];
});

describe('displayBusDetailsAndSeats', () => {
    it('should display bus details and seats', () => {
        const bus = {
            status: 'ON TIME',
            reserved_seats: [1, 2, 3],
            max_seats: 10
        };
        displayBusDetailsAndSeats(bus);
        expect(document.getElementById('reserveButton').disabled).toBe(false);
        expect(document.getElementById('reserveButton').textContent).toBe('Reserve');
    });

    it('should disable the reserve button if the bus status is LEFT or LEAVING', () => {
        const bus = {
            status: 'LEFT',
            reserved_seats: [1, 2, 3],
            max_seats: 10
        };
        displayBusDetailsAndSeats(bus);
        expect(document.getElementById('reserveButton').disabled).toBe(true);
    });

    it('should disable the reserve button and change its text if all seats are taken', () => {
        const bus = {
            status: 'ON TIME',
            reserved_seats: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            max_seats: 10
        };
        displayBusDetailsAndSeats(bus);
        expect(document.getElementById('reserveButton').disabled).toBe(true);
        expect(document.getElementById('reserveButton').textContent).toBe('No seats available');
    });
});

describe('resetReservationForm', () => {
    it('should reset the reservation form', () => {
        resetReservationForm();
        expect(document.getElementById('seatNumber').value).toBeNull();
        expect(document.getElementById('fullName').value).toBe('');
    });
});