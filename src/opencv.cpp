#include "opencv.hpp"
#include <opencv2/opencv.hpp>

using namespace cv;

opencv::opencv(/* args */)
{
}

int opencv::show_image(std::string file) {
    auto image = imread( file, 1 );
    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}

int opencv::show_video(std::string file) {

    auto cap = VideoCapture("/home/haoshuai/视频/1.mkv");
    if (!cap.isOpened()) {
        printf("No video data \n");
        return -1;
    }
    double fps = cap.get(CAP_PROP_FPS);
    double len = cap.get(CAP_PROP_FRAME_COUNT);
    double f_w = cap.get(CAP_PROP_FRAME_WIDTH);
    double f_h = cap.get(CAP_PROP_FRAME_HEIGHT);
    printf("fps: %f len: %f w: %d h: %d\n", fps, len, f_w, f_w);
    Mat frame;
    while (cap.read(frame))
    {
        imshow("Display Image",frame);
        waitKey(int(fps));
    }
    return 0;
}

opencv::~opencv()
{
}
