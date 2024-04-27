
import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('move_turtle', anonymous=True)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    twist = Twist()
    
    twist.linear.x = 2.5  # Velocidad lineal hacia adelante
    twist.angular.z = 5  # Velocidad angular (giro)

    rate = rospy.Rate(30)  # 10 Hz



    rospy.sleep(2)




    # Detiene la tortuga
    twistd = Twist()
    twistd.linear.x = 0.0
    twistd.angular.z = 0.0
    pub.publish(twistd)
    
    # Publica el mensaje de Twist en el topic "/turtle1/cmd_vel"
    pub.publish(twist)
    rospy.sleep(30)
    # Espera hasta el próximo ciclo de publicación
        
    pub.publish(twistd)

    rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass