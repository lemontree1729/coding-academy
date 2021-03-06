package d019;

class Exercise6_04 {
    public static void main(String[] args) {
        Student s = new Student();
        s.name = "john do";
        s.ban = 1;
        s.no = 1;
        s.kor = 100;
        s.eng = 60;
        s.math = 76;

        System.out.println("name: " + s.name);
        System.out.println("total: " + s.getTotal());
        System.out.println("average: " + s.getAverage());
    }
}

class Student {
    String name;
    int ban;
    int no;
    int kor;
    int eng;
    int math;

    int getTotal() {
        return kor + eng + math;
    }

    float getAverage() {
        return Math.round(getTotal() * 100 / 3.0) / 100F;
        // return (int) (getTotal() * 100 / 3F + 0.5F) / 100F;
    }
}