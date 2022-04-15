
// This problem was asked by Microsoft.
// 
// Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.
// 
// Bonus: When, during the course of a day, will the angle be zero?


fn clock_angle(hours: i32, minutes: i32) -> i32 {
    let hour_angle = (hours as f64 / 12.0) * 360.0;
    let minute_angle = (minutes as f64 / 60.0) * 360.0;

    // We will measure the angle between the hands as bounded [0, 180]
    let mut result = hour_angle - minute_angle;
    if result < -180.0 {
        result += 360.0;
    }
    if result > 180.0 {
        result -= 360.0;
    }
    result.abs().round() as i32
}

fn main() {
    assert_eq!(clock_angle(12, 0), 0);
    assert_eq!(clock_angle(6, 0), 180);
    assert_eq!(clock_angle(3, 0), 90);
    assert!(clock_angle(3, 15) < 90);
    assert!(clock_angle(3, 15) > 45);
}
