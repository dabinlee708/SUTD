    int i;
    int j;
    int k = 0;
    
    List<Point3d> pointList00 = new List<Point3d>();
    List<Point3d> pointLIst01 = new List<Point3d>();
    List<Line> lineList00 = new List<Line>();

    for(j = 0; j < ry; j++){
      for(i = 0; i < rx; i++){
        pt.Add(new Point3d(i, j, 0.0));
        if(j != 0){
          ln.Add(new Line(pt[k], pt[k - rx]));
        }
        if(i != 0){
          ln.Add(new Line(pt[k], pt[k - 1]));
        }
        if(i!= 0 && j!= 0){
          Point3d mid = MidPt(pt[k], pt[k - rx - 1]);
          ln.Add(new Line(pt[k], mid + vec));
          ln.Add(new Line(mid + vec, pt[k - rx - 1]));
        }
        if(i<rx - 1 && j != 0){
          Point3d mid2 = MidPt(pt[k], pt[k - rx + 1]);
          ln.Add(new Line(pt[k], mid2 + vec));
          ln.Add(new Line(mid2 + vec, pt[k - rx + 1]));
        }

        if(j > 1 && i != 0){
          Point3d middle = MidPt(pt[k], pt[k - rx - 1]);
          Point3d middle2 = MidPt(pt[k - rx], pt[k - rx - rx - 1]);
          ln.Add(new Line(middle + vec, middle2 + vec));

        }

        if(j != 0 && i > 1){
          Point3d middle3 = MidPt(pt[k], pt[k - rx - 1]);
          Point3d middle4 = MidPt(pt[k - 1], pt[k - rx - 2]);
          ln.Add(new Line(middle3 + vec, middle4 + vec));
        }

        k++;
      }
    }

    A = pt;
    B = pt2;
    C = ln;