import sys;

class Main(object):
    def putc(self, char: str) -> int:
        return sys.stdout.write(char[0]);

    def puts(self, string: str) -> int:
        amount_of_bytes_written: int = 0;

        for i in range(0, len(string)):
            amount_of_bytes_written = amount_of_bytes_written + self.putc(string[i]);

        return amount_of_bytes_written+1;

    def _main(self) -> int:
        hello: list = [None, None, None, None, None, None, None, None, None, None, None, None, None];
        for i in range(0, 13):
            hello[i] = "Hello, world!"[i];

        for i in range(0, 13):
            self.puts(hello[i]);
        self.putc(chr(13));
        self.putc(chr(10));
        return 0;

    def ___PosixProcessStartup(self) -> None:
        self._main();

if __name__ == "__main__":
    sys.exit(Main()._Main___PosixProcessStartup());
