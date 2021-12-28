# Face recognition and pose recognition for a Socially Assistive Robot

The use of socially assistive robots in Applied Behavioral Analysis (ABA) therapy has proven to help therapists focus more on the session rather than keeping a track of the child's progress. For this project, we consider ABA therapy sessions conducted for Autism Spectrum Disorder. The scenario considered here involves the use of PABI (Penguin for Autism Behavioral Intervention), a socially assistive robot created specifically to assist  in ABA therapies. It is equipped with Intel REalSense camera which is used for data recording, data logging and further analysis. Face and pose recognition can help determine behavioral aspects of patients during ABA therapy. 

## Face Recognition

Face recognition at the beginning of a therapy session is necessary for storing the patient's data to their respective folders. For this, two approaches were used. First was using FaceNET model which resulted in 100% accuracy for the collected data. However to reduce the computational cost for larger dataset, Principal Component Analysis was implemented. Using this, 97% accuracy was achieved. 

## Pose Recognition

For this, MediaPipe API was used which resulted in an accuracy of 100%. Using this, it can be determined whether the person in focus is 'studying' or 'looking here and there'.

![Getting Started](./Pose_recognition/pose1.jpg)

## Application

These results can help derive conclusions regarding the attention span of the patient. This project is a foundation for a system which can be used to infer behavioral changes and help decide the course of future therapy sessions.