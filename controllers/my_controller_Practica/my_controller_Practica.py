from controller import Robot,Camera
import cv2
import numpy as np
def run_robot(robot):
    time_step=32
    max_speed=6.28
    lm=robot.getMotor('left wheel motor')
    rm=robot.getMotor('right wheel motor')
    lm.setPosition(float('inf'))
    rm.setPosition(float('inf'))
    lm.setVelocity(0.0)
    lm.setVelocity(0.0)
    # sensores
    l_ir=robot.getDistanceSensor('ir0')
    r_ir=robot.getDistanceSensor('ir1')
    l_ir.enable(time_step)
    r_ir.enable(time_step)
    
    cm=robot.getCamera("camera");
    Camera.enable(cm,time_step);
    
    while robot.step(time_step)!=-1:
    
        Camera.getImage(cm)
        Camera.saveImage(cm,"color.png",1)
        frame=cv2.imread("color.png")
        #
        l_ir_value=l_ir.getValue()
        r_ir_value=r_ir.getValue()
        print("left:{} right:{}".format(l_ir_value,r_ir_value))
        #
        ls=max_speed*0.3
        rs=max_speed*0.3
        #
 
        #
        if(6<r_ir_value<27)and (6<l_ir_value<27): 
            lm.setVelocity(ls)
            rm.setVelocity(rs)
        else:
            if(r_ir_value>27):
                print("ir izquierda:")
                ls=-max_speed
            elif(l_ir_value<27):
                print("ir derecha:")
                rs=-max_speed
            lm.setVelocity(-ls)
            rm.setVelocity(rs)
            
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([50,100,100])
        upper_blue = np.array([35,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        cv2.imshow('frame',frame)
        cv2.waitKey(time_step)
if __name__ == "__main__":
    my_robot=Robot()
    run_robot(my_robot)
