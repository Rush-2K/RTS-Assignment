
from controller import Robot

def run_robot(robot):

    time_step = 32
    max_speed = 6.28
    
    #Motors
    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    #enable ir sensors
    left_ir = robot.getDistanceSensor('ir0')
    left_ir.enable(time_step)
    
    right_ir = robot.getDistanceSensor('ir1')
    right_ir.enable(time_step)
    
    #enable accelerometer
    acc_sensor = robot.getAccelerometer('accelerometer')
    acc_sensor.enable(time_step)
    
    #enable proximity sensor
    prox_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[ind].enable(time_step)
    
    #step simulation
    while robot.step(time_step) != -1:
        print('test')
        # for ind in range(8):
            # if 
            # print('ind: {}, val: {}'.format(ind, prox_sensors[ind].getValue()))
        
        #detect anomalies
        left_anom = prox_sensors[5].getValue() > 80
        right_anom = prox_sensors[2].getValue() > 80
        
        if left_anom:
            print("Branches is out on left")   
        
        if right_anom:
            print("Branches is out on right")
        
        #read acc sensors
        acc_sensor_value = acc_sensor.getValues()
        
        round_acc_value = [f"{num:.2f}" for num in acc_sensor_value]
        
        # print("IMU Sensor value: {} ".format(round_acc_value))
        
        #read ir sensors
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        
        print("left: {} right: {}".format(left_ir_value, right_ir_value))
        print("acc sensor: ", acc_sensor_value)
    
        left_speed = max_speed * 0.25
        right_speed = max_speed * 0.25
        
        if(left_ir_value > right_ir_value) and (6 < left_ir_value < 15):
            # print("Go left")
            left_speed = -max_speed
        elif(right_ir_value > left_ir_value) and (6 < right_ir_value < 15):
            # print("Go right")
            right_speed = -max_speed
            
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)